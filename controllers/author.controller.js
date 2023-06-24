const errorHandler = require("../helpers/error_handler");
const Author = require("../model/Author");
const bcrypt = require("bcrypt");
const myJwt = require("../services/JwtService");
const config = require("config");
const uuid = require("uuid");
const MailService = require("../services/MailService");

const addAuthor = async (req, res) => {
  try {
    const {
      author_first_name,
      author_last_name,
      author_nick_name,
      author_password,
      author_email,
      author_phone,
      author_info,
      author_position,
      author_photo,
      is_expert,
    } = req.body;

    const author = await Author.findOne({ author_email });
    if (author) {
      return res.status(400).send({ message: "Bunday author kiritilgan" });
    }

    const hashed_password = await bcrypt.hash(author_password, 7);
    const author_activation_link = uuid.v4();

    const newAuthor = await Author({
      author_first_name,
      author_last_name,
      author_nick_name,
      author_password: hashed_password,
      author_email,
      author_phone,
      author_info,
      author_position,
      author_photo,
      is_expert,
      author_activation_link,
    });
    await newAuthor.save();

    await MailService.sendActivationMail(
      author_email,
      `${config.get("api_url")}/author/activate/${author_activation_link}`
    );

    const payload = {
      id: newAuthor._id,
      is_expert: newAuthor.is_expert,
      authorRoles: ["READ", "WRITE"],
      author_is_active: newAuthor.author_is_active,
    };

    const tokens = myJwt.generateToken(payload);
    newAuthor.author_token = tokens.refreshToken;
    await newAuthor.save();

    res.cookie("refreshToken", tokens.refreshToken, {
      maxAge: config.get("refresh_ms"),
      httpOnly: true,
    });

    res.status(200).send({ ...tokens, author: payload });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getAllAuthor = async (req, res) => {
  try {
    const authors = await Author.find({});
    if (authors.length < 1) {
      return res.status(400).send({ message: "Birorta ham author topilmadi" });
    }
    res.json({ data: authors });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getAuthorById = async (req, res) => {
  const id = req.params.id;
  try {
    const author = await Author.find({ _id: id });
    if (author.length < 1) {
      return res.status(400).send({ message: "Author topilmadi" });
    }
    res.json({ author });
  } catch (error) {
    errorHandler(res, error);
  }
};

const editAuthor = async (req, res) => {
  try {
    const id = req.params.id;
    const {
      author_first_name,
      author_last_name,
      author_nick_name,
      author_password,
      author_email,
      author_phone,
      author_info,
      author_position,
      author_photo,
      is_expert,
    } = req.body;

    const editing = await Author.updateOne({ _id: id }, [
      {
        $set: {
          author_first_name,
          author_last_name,
          author_nick_name,
          author_password,
          author_email,
          author_phone,
          author_info,
          author_position,
          author_photo,
          is_expert,
        },
      },
    ]);
    res.json(editing);
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteAuthor = async (req, res) => {
  try {
    const id = req.params.id;
    if (id !== req.author.id) {
      return res.status(401).send({ message: "Sizda bunady huquq yo'q" });
    }

    const result = await Author.findOne({ _id: id });
    if (result == null)
      return res.status(400).send({ message: "Id is incorrect" });
    await Author.findByIdAndDelete(id);
    res.status(202).send({ message: "OK.  Author is deleted" });
  } catch (error) {
    console.log(error);
    errorHandler(res, error);
  }
};

const logoutAuthor = async (req, res) => {
  const { refreshToken } = req.cookies;
  let author;
  if (!refreshToken)
    return res.status(400).send({ message: "Token topilmadi" });
  author = await Author.findOneAndUpdate(
    { author_token: refreshToken },
    { author_token: "" },
    { new: true }
  );
  if (!author) return res.status(400).send({ message: "Token topilmadi" });

  res.clearCookie("refreshToken");
  res.status(200).send({ author });
};

const loginAuthor = async (req, res) => {
  try {
    const { author_email, author_password } = req.body;
    const author = await Author.findOne({ author_email });
    if (!author) {
      return res
        .status(400)
        .send({ message: "Invalid authorization email or password " });
    }
    const validPassword = bcrypt.compareSync(
      author_password, //?                           Plain password
      author.author_password //?                     Hashed password
    );
    if (!validPassword) {
      return res
        .status(400)
        .send({ message: "Invalid authorization email or password " });
    }

    const payload = {
      id: author.id,
      is_export: author.is_expert,
      exuthorRoles: ["READ", "WRITE"],
    };
    const tokens = myJwt.generateToken(payload);

    author.author_token = tokens.refreshToken;
    await author.save();
    res.cookie("refreshToken", tokens.refreshToken, {
      maxAge: config.get("refresh_ms"),
      httpOnly: true,
    });
    res.status(200).send({ ...tokens });
  } catch (error) {
    errorHandler(res, error);
  }
};

const refreshAuthorToken = async (req, res) => {
  const { refreshToken } = req.cookies;
  if (!refreshToken)
    return res.status(400).send({ message: "Token not found" });

  const authorDataFromCookie = await myJwt.verifyRefresh(refreshToken);
  const authorDataFromDB = await Author.findOne({ author_token: refreshToken });
  console.log(authorDataFromDB);
  if (!authorDataFromCookie || !authorDataFromDB) {
    return res.status(400).send({ message: "Author is not found" });
  }
  const auth = await Author.findById(authorDataFromCookie.id);
  if (!auth) return res.status(400).send({ message: "ID invalid" });

  const payload = {
    id: auth._id,
    is_expert: auth.is_expert,
    authorRoles: ["READ", "WRITE"],
  };

  const tokens = myJwt.generateTokens(payload);
  auth.author_token = tokens.refreshToken;
  await auth.save();
  res.cookie("refreshToken", tokens.refreshToken, {
    maxAge: config.get("refresh_ms"),
    httpOnly: true,
  });
  res.status(200).send({ ...tokens });
};

const authorActivate = async (req, res) => {
  try {
    const author = await Author.findOne({
      author_activation_link: req.params.link,
    });
    if (!author) {
      return res.status(400).send({ message: "Bunday author topilmadi" });
    }

    if (author.author_is_active) {
      return res.status(400).send({ message: "Author already activated" });
    }

    author.author_is_active = true;
    await author.save();
    res.status(200).send({
      author_is_active: author.author_is_active,
      message: "Author activated",
    });
  } catch (error) {
    errorHandler(res, error);
  }
};

module.exports = {
  getAllAuthor,
  addAuthor,
  getAuthorById,
  editAuthor,
  deleteAuthor,
  loginAuthor,
  logoutAuthor,
  refreshAuthorToken,
  authorActivate,
};
