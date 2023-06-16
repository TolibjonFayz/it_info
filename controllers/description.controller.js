const errorHandler = require("../helpers/error_handler");
const Description = require("../model/Description");

const addDescription = async (req, res) => {
  try {
    const { description, category_id } = req.body;
    const newDescription = await Description({
      description: description,
      category_id: category_id,
    });
    await newDescription.save();
    res.json({ message: "Successfully addedd" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getAllDescriptions = async (req, res) => {
  try {
    const descriptions = await Description.find({}).populate("category_id");
    if (descriptions.length < 1) {
      return res.status(400).send({ message: "Any description not found" });
    }
    res.json(descriptions);
  } catch (error) {
    errorHandler(res, error);
  }
};

const getDescriptionById = async (req, res) => {
  try {
    const id = req.params.id;
    const description = await Description.find({ _id: id });
    if (description.length < 1) {
      return res.status(400).send({ message: "Description not found" });
    }
    res.json(description);
  } catch (error) {
    errorHandler(res, error);
  }
};

const getDescriptionByLetter = async (req, res) => {
  try {
    const letter = req.params.letter;
    const description = await Description.find({ letter });
    if (description.length < 1) {
      return res.status(400).send({ message: "Description not found" });
    }
    res.json(description);
  } catch (error) {
    errorHandler(res, error);
  }
};

const editDescription = async (req, res) => {
  try {
    const id = req.params.id;
    const { description, category_id } = req.body;

    const editing = await Description.updateOne({ _id: id }, [
      { $set: { description: description, category_id: category_id } },
    ]);
    res.json(editing);
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteDescription = async (req, res) => {
  try {
    const id = req.params.id;
    const deleted = await Description.deleteOne({ _id: id });
    res.json(deleted);
  } catch (error) {
    errorHandler(error);
  }
};

module.exports = {
  addDescription,
  getAllDescriptions,
  getDescriptionById,
  getDescriptionByLetter,
  editDescription,
  deleteDescription,
};
