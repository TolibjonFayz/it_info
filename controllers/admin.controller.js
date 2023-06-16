const errorHandler = require("../helpers/error_handler");
const Admin = require("../model/Admin");
const { adminValidation } = require("../validations/admin");
const bcrypt = require("bcrypt");

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
    const { error, value } = adminValidation(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }
    const {
      admin_name,
      admin_email,
      admin_password,
      admin_is_active,
      admin_is_creator,
      created_data,
      updated_at,
    } = value;

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

module.exports = { getAllAdmins, addAdmin, getAdminById, editAdmin };
