const express = require("express");
const {
  getAllAdmins,
  addAdmin,
  getAdminById,
  editAdmin,
} = require("../controllers/admin.controller");
const router = express.Router();

router.get("/", getAllAdmins);
router.post("/", addAdmin);
router.get("/:id", getAdminById);
router.put("/:id", editAdmin);

module.exports = router;
