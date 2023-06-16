const express = require("express");
const {
  addDescription,
  getAllDescriptions,
  getDescriptionById,
  getDescriptionByLetter,
  editDescription,
  deleteDescription,
} = require("../controllers/description.controller");

const router = express.Router();

//handlar
router.post("/", addDescription);
router.get("/", getAllDescriptions);
router.get("/:id", getDescriptionById);
router.get("/letter/:letter", getDescriptionByLetter);
router.put("/:id", editDescription);
router.delete("/:id", deleteDescription);

module.exports = router;
