const express = require("express");
const {
  getAllTermin,
  addTermin,
  getTerminByLetter,
  getTerminById,
  editTermin,
  deleteTerminById,
} = require("../controllers/dictionary.controllers");

const router = express.Router();

router.get("/", getAllTermin);
router.post("/", addTermin);
router.get("/letter/:letter", getTerminByLetter);
router.get("/:id", getTerminById);
router.put("/:id", editTermin);
router.delete("/:id", deleteTerminById);

module.exports = router;
