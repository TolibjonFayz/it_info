const errorHandler = require("../helpers/error_handler");
const User = require("../model/User");
const { userValidation } = require("../validations/user");
const bcrypt = require("bcrypt");
const myJwt = require("../services/JwtService");
const config = require("config");
const uuid = require("uuid");
const MailService = require("../services/MailService");

const getAllUsers = async (req, res) => {
  try {
    const users = await User.find({});
    if (users.length < 1) {
      return res.status(400).send({ message: "Any user not found!" });
    }
    res.json({ users });
  } catch (error) {
    errorHandler(res, error);
  }
};

const addUser = async (req, res) => {
  try {
    const { error, value } = userValidation(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const {
      user_name,
      user_email,
      user_password,
      user_is_active,
      user_is_creator,
      created_data,
      updated_at,
    } = value;

    const user = await User.find({ user_email });
    const user_activation_link = uuid.v4();

    if (user.length > 1) {
      console.log(user);
      return res.status(400).send({ messaeg: "Bunday user kiritilgan" });
    }

    const hiddenPassword = bcrypt.hashSync(user_password, 8);
    const new_user = await User({
      user_name,
      user_email,
      user_password: hiddenPassword,
      user_is_active,
      user_is_creator,
      created_data,
      updated_at,
      user_activation_link,
    });

    await new_user.save();

    await MailService.sendActivationMail(
      user_email,
      `${config.get("api_url")}/user/activate/${user_activation_link}`
    );

    const payload = {
      id: new_user._id,
      user_is_creator: new_user.user_is_creator,
      authorRoles: ["READ", "WRITE"],
      user_is_active: new_user.user_is_active,
    };

    const tokens = myJwt.generateToken(payload);
    new_user.user_token = tokens.refreshToken;
    await new_user.save();

    res.cookie("refreshToken", tokens.refreshToken, {
      maxAge: config.get("refresh_ms"),
      httpOnly: true,
    });
    return res.status(200).send({ message: "New user added successfully" });
  } catch (error) {
    console.log(error);
    errorHandler(res, error);
  }
};

const getUsetById = async (req, res) => {
  try {
    const id = req.params.id;
    const user = await User.find({ _id: id });
    res.json({ user });
  } catch (error) {
    errorHandler(res, error);
  }
};

const edituser = async (req, res) => {
  try {
    const id = req.params.id;
    const {
      user_name,
      user_email,
      user_password,
      user_is_active,
      user_is_creator,
      created_data,
      updated_at,
    } = req.body;

    const editingUser = await User.updateOne({ _id: id }, [
      {
        $set: {
          user_name,
          user_email,
          user_password,
          user_is_active,
          user_is_creator,
          created_data,
          updated_at,
        },
      },
    ]);
    res.json({ message: "User successfully updated!" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteuser = async (req, res) => {
  try {
    const id = req.params.id;
    const deleting = await User.deleteMany({ _id: id });
    res.json({ message: "User successfully deleted!" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const loginUser = async (req, res) => {
  try {
    const { user_email, user_password } = req.body;
    const user = await User.findOne({ user_email });
    if (!user)
      return res.status(400).send({ message: "Invalid email or password" });

    const validPassword = bcrypt.compareSync(user_password, user.user_password);

    if (!validPassword) {
      return res.status(400).send({ message: "Invalid email or password" });
    }
    const payload = {
      id: user.id,
      user_is_active: user.user_is_active,
      user_is_creator: user.user_is_creator,
      exuthorRoles: ["READ", "WRITE"],
    };

    const tokens = myJwt.generateToken(payload);

    user.user_token = tokens.refreshToken;
    await user.save();

    res.cookie("refreshToken", tokens.refreshToken, {
      maxAge: config.get("refresh_ms"),
      httpOnly: true,
    });
    res.status(200).send({ ...tokens });
  } catch (error) {
    // console.log(error);
    errorHandler(res, error);
  }
};

const logoutUser = async (req, res) => {
  const { refreshToken } = req.cookies;
  let user;
  if (!refreshToken)
    return res.status(400).send({ message: "Token topilmadi!" });
  user = await User.findOneAndUpdate(
    { user_token: refreshToken },
    { user_token: "" },
    { new: true }
  );
  // console.log(user);
  if (!user) return res.status(400).send({ message: "Token topilmadi" });

  res.clearCookie("refreshToken");
  res.status(200).send({ user });
};

const userActivate = async (req, res) => {
  try {
    const user = await User.findOne({
      user_activation_link: req.params.link,
    });
    if (!user) {
      return res.status(400).send({ message: "User not found" });
    }

    if (user.user_is_active) {
      return res.status(400).send({ message: "User already activated" });
    }

    user.user_is_active = true;
    await user.save();
    res.status(200).send({
      user_is_active: user.user_is_active,
      message: "User activated",
    });
  } catch (error) {
    errorHandler(res, error);
  }
};

module.exports = {
  getAllUsers,
  addUser,
  getUsetById,
  edituser,
  deleteuser,
  loginUser,
  logoutUser,
  userActivate,
};
