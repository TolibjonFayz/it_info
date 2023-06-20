const errorHandler = require("../helpers/error_handler");
const Admin = require("../model/Admin");
const { adminValidation } = require("../validations/admin");
const bcrypt = require("bcrypt");
const myJwt = require("../services/JwtService");
const config = require("config");

const getAllAdmins = async (req, res) => {
  try {
    const admins = await Admin.find({});
    if (admins.length < 1) {
      return res.status(400).send({ message: "Any admin not found!" });
    }
    res.json({ admins });
  } catch (error) {
    errorHandler(res, error);
  }
};

const addAdmin = async (req, res) => {
  try {
    const {
      admin_name,
      admin_email,
      admin_password,
      admin_is_active,
      admin_is_creator,
      created_data,
      updated_at,
    } = req.body;

    const admin = await Admin.find({ admin_email });

    if (!admin) {
      return res.status(400).send({ message: "Bunday admin kiritilgan" });
    }

    const hashed_password = bcrypt.hashSync(admin_password, 8);

    const newAdmin = await Admin({
      admin_name,
      admin_email,
      admin_password: hashed_password,
      admin_is_active,
      admin_is_creator,
      created_data,
      updated_at,
    });

    await newAdmin.save();
    res.status(200).send({ message: "New admin added successfully" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getAdminById = async (req, res) => {
  try {
    const id = req.params.id;
    const admin = await Admin.find({ _id: id });
    if (!admin) {
      return res.status(400).send({ message: "Admin not found at this id!" });
    }
    res.json({ admin });
  } catch (error) {
    errorHandler(res, error);
  }
};

const editAdmin = async (req, res) => {
  try {
    const id = req.params.id;
    const {
      admin_name,
      admin_email,
      admin_password,
      admin_is_active,
      admin_is_creator,
      created_data,
      updated_at,
    } = req.body;

    const editingAdmin = await Admin.updateOne({ _id: id }, [
      {
        $set: {
          admin_name,
          admin_email,
          admin_password,
          admin_is_active,
          admin_is_creator,
          created_data,
          updated_at,
        },
      },
    ]);
    res.json({ editingAdmin });
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteAdmin = async (req, res) => {
  try {
    const id = req.params.id;
    const deletingAdmin = await Admin.deleteOne({ _id: id });
    res.json(deletingAdmin);
  } catch (error) {
    errorHandler(res, error);
  }
};

const loginAdmin = async (req, res) => {
  try {
    const { admin_email, admin_password } = req.body;
    const admin = await Admin.findOne({ admin_email });
    if (!admin) {
      return res.status(400).send({ message: "Invalid email or password" });
    }

    const validPassword = bcrypt.compareSync(
      admin_password,
      admin.admin_password
    );

    if (!validPassword) {
      return res.status(400).send({ message: "Invalid email or password" });
    }

    const payload = {
      id: admin.id,
      admin_is_active: admin.admin_is_active,
      admin_is_creator: admin.admin_is_creator,
      exuthorRoles: ["READ", "DELETE"],
    };
    const tokens = myJwt.generateToken(payload);

    admin.admin_token = tokens.refreshToken;
    await admin.save();

    res.cookie("refreshToken", tokens.refreshToken, {
      maxAge: config.get("refresh_ms"),
      httpOnly: true,
    });
    res.status(200).send({ ...tokens });
  } catch (error) {
    errorHandler(res, error);
  }
};

const logoutAdmin = async (req, res) => {
  const { refreshToken } = req.cookies;
  let admin;
  if (!refreshToken)
    return res.status(400).send({ message: "Token topilmadi!" });
  admin = await Admin.findOneAndUpdate(
    { admin_token: refreshToken },
    { admin_token: "" },
    { new: true }
  );
  if (!admin) return res.status(400).send({ message: "Token topilmadi" });

  res.clearCookie("refreshToken");
  res.status(200).send({ admin });
};

module.exports = {
  getAllAdmins,
  addAdmin,
  getAdminById,
  editAdmin,
  deleteAdmin,
  loginAdmin,
  logoutAdmin,
};
