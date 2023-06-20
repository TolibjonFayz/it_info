const express = require("express");
const {
  getAllAdmins,
  addAdmin,
  getAdminById,
  editAdmin,
  deleteAdmin,
  loginAdmin,
  logoutAdmin,
} = require("../controllers/admin.controller");
const adminPolice = require("../middleware/adminPolice");

const Validator = require("../middleware/validator");

const router = express.Router();

//handlers
router.get("/", adminPolice, getAllAdmins);
router.post("/", Validator("admin"), addAdmin);
router.get("/:id", getAdminById);
router.put("/:id", editAdmin);
router.delete("/:id", deleteAdmin);
router.post("/login", Validator("admin_email_pass"), loginAdmin);
router.post("/logout", logoutAdmin);

module.exports = router;
