const errorHandler = require("../helpers/error_handler");
const Author = require("../model/Author");
const { authorValidation } = require("../validations/author");
const bcrypt = require("bcrypt");
const myJwt = require("../services/JwtService");
const config = require("config");

const addAuthor = async (req, res) => {
  try {
    const { error, value } = authorValidation(req.body);
    if (error) {
      return res.status(404).send({ message: error.details[0].message });
    }

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
    } = value;

    const author = await Author.findOne({ author_email });
    if (author) {
      return res.status(400).send({ message: "Bunday author kiritilgan" });
    }

    const hashed_password = await bcrypt.hash(author_password, 7);

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
    });
    await newAuthor.save();
    res.status(200).send({ message: "Yangi author qo'shildi" });
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
    res.json({ authors });
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
    const deleting = await Author.deleteOne({ _id: id });
    res.json(deleting);
  } catch (error) {
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

module.exports = {
  getAllAuthor,
  addAuthor,
  getAuthorById,
  editAuthor,
  deleteAuthor,
  loginAuthor,
  logoutAuthor,
};
