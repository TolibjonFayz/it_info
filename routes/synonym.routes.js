const express = require("express");
const {
  getAllSynonyms,
  addSynonym,
  getSynonymById,
  editSynonym,
  deleteSynonym,
} = require("../controllers/synonym.controllers");

const router = express.Router();

//Yo'llar
router.get("/", getAllSynonyms);
router.post("/", addSynonym);
router.get("/:id", getSynonymById);
router.put("/:id", editSynonym);
router.delete("/:id", deleteSynonym);

module.exports = router;
