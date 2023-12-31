const express = require("express");
const {
  getAllUsers,
  addUser,
  getUsetById,
  edituser,
  deleteuser,
  loginUser,
  logoutUser,
  userActivate,
} = require("../controllers/user.controller");
const router = express.Router();

router.get("/", getAllUsers);
router.post("/", addUser);
router.get("/:id", getUsetById);
router.put("/:id", edituser);
router.delete("/:id", deleteuser);
router.post("/login", loginUser);
router.post("/logout", logoutUser);
router.get("/activate/:id", userActivate);

module.exports = router;
