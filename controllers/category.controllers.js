const errorHandler = require("../helpers/error_handler");
const Category = require("../model/Category");
const { categoryvalidation } = require("../validations/category");

const getAllCategory = async (req, res) => {
  try {
    const categoties = await Category.find({});
    if (categoties.length < 1) {
      return res
        .status(400)
        .send({ message: "Birorta ham category topilmadi" });
    }
    res.json({ categoties });
  } catch (error) {
    errorHandler(res, error);
  }
};

const addCategory = async (req, res) => {
  try {
    const { error, value } = categoryvalidation(req.body);
    if (error) {
      return res.status(400).send({ message: error.details[0].message });
    }

    const { category_name, parent_category_id } = req.body;
    const newCategory = await Category({
      category_name: category_name,
      parent_category_id: parent_category_id,
    });
    await newCategory.save();
    res.status(200).send({ message: "Yangi category qo'shildi" });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getCategoryById = async (req, res) => {
  const id = req.params.id;
  try {
    const category = await Category.find({ _id: id });
    if (category.length < 1) {
      return res.status(400).send({ message: "Category topilmadi" });
    }
    res.json({ category });
  } catch (error) {
    errorHandler(res, error);
  }
};

const getCategoryByLetter = async (req, res) => {
  try {
    const letter = req.params.letter;
    const result = await Category.find({ letter });
    if (result.length < 1) {
      return res.status(400).send({ message: "Birorta category topilmadi!" });
    }
    res.json(result);
  } catch (error) {
    errorHandler(res, error);
  }
};

const editCategory = async (req, res) => {
  console.log("kb");
  try {
    const id = req.params.id;
    const { category_name, parent_category_id } = req.body;
    const updated = await Category.updateOne({ _id: id }, [
      {
        $set: {
          category_name: category_name,
          parent_category_id: parent_category_id,
        },
      },
    ]);
    res.json(updated);
  } catch (error) {
    errorHandler(res, error);
  }
};

const deleteCategory = async (req, res) => {
  try {
    const id = req.params.id;
    const deleted = await Category.deleteOne({ _id: id });
    res.json(deleted);
  } catch (error) {
    errorHandler(res, error);
  }
};

module.exports = {
  getAllCategory,
  addCategory,
  getCategoryById,
  getCategoryByLetter,
  editCategory,
  deleteCategory,
};
