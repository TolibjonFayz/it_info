const express = require("express");
const {
  getAllSynonyms,
  addSynonym,
  getSynonymById,
} = require("../controllers/synonym.controllers");

const router = express.Router();

//Yo'llar
router.get("/", getAllSynonyms);
router.post("/", addSynonym);
router.get("/:id", getSynonymById);

module.exports = router;
