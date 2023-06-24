const errorHandler = require("../helpers/error_handler");
const Dictionary = require("../model/Dictionary");

const addTermin = async (req, res) => {
  try {
    const { term } = req.body;
    const dict = await Dictionary.findOne({
      term: { $regex: term, $options: "i" },
    });
    if (dict) {
      return res
        .status(400)
        .send({ message: "Bunday termin avval keltirilgan" });
    }
    const newTerm = await Dictionary({
      term: term,
      letter: term[0],
    });
    await newTerm.save();
    res.status(200).send({ message: "Yangi termin qo'shildi" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getAllTermin = async (req, res) => {
  try {
    const terms = await Dictionary.find({});
    if (!terms) {
      return res.status(400).send({ message: "Birorta ham termin topilmadi" });
    }
    res.json({ data: terms });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getTerminByLetter = async (req, res) => {
  try {
    const letter = req.params.letter;
    const terms = await Dictionary.find({ letter });

    if (terms.length < 1) {
      return res.status(400).send({ message: "Birorta termin topilmadi" });
    }

    res.json({ terms });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getTerminById = async (req, res) => {
  try {
    const id = req.params.id;
    const term = await Dictionary.find({ _id: id });
    if (term.length < 1) {
      return res.status(400).send({ message: "Termin topilmadi" });
    }
    res.json(term);
  } catch (error) {
    errorHandler(res, error);
  }
};

const editTermin = async (req, res) => {
  const id = req.params.id;
  const { term } = req.body;
  try {
    const editedTermin = await Dictionary.updateOne({ _id: id }, [
      { $set: { term: term, letter: term[0] } },
    ]);
    res.json(editedTermin);
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteTerminById = async (req, res) => {
  const id = req.params.id;
  try {
    const deletedTerm = await Dictionary.deleteOne({ _id: id });
    res.json(deletedTerm);
  } catch (error) {
    errorHandler(res, error);
  }
};
module.exports = {
  addTermin,
  getAllTermin,
  getTerminByLetter,
  getTerminById,
  editTermin,
  deleteTerminById,
};
