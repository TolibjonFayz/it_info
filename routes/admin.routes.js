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
const { route } = require("./author.routes");

const router = express.Router();

//handlers
router.get("/", adminPolice, getAllAdmins);
router.post("/", addAdmin);
router.get("/:id", getAdminById);
router.put("/:id", editAdmin);
router.delete("/:id", deleteAdmin);
router.post("/login", loginAdmin);
router.post("/logout", logoutAdmin);

module.exports = router;
