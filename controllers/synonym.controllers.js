const Synonym = require("../model/Synonm");
const errorHandler = require("../helpers/error_handler");
const getAllSynonyms = async (req, res) => {
  try {
    const synonyms = await Synonym.find({});
    if (synonyms.length < 1) {
      return res.status(400).send({ message: "Any synonyms not found" });
    }
    res.json(synonyms);
  } catch (error) {
    errorHandler(res, error);
  }
};

const addSynonym = async (req, res) => {
  try {
    const { desc_id, dict_id } = req.body;
    const adding = await Synonym({
      desc_id: desc_id,
      dict_id: dict_id,
    });
    await adding.save();
    res.json({ message: "Synonym successfully added" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getSynonymById = async (req, res) => {
  try {
    const id = req.params.id;
    const synonym = await Synonym.find({ _id: id });
    if (!synonym) {
      return res
        .status(400)
        .send({ messaeg: "Synonym is not found at this ID" });
    }
    res.json(synonym);
  } catch (error) {
    errorHandler(res, error);
  }
};

module.exports = { getAllSynonyms, addSynonym, getSynonymById };
