const express = require("express");
const {
  getAllCategory,
  addCategory,
  getCategoryById,
  getCategoryByLetter,
  editCategory,
  deleteCategory,
} = require("../controllers/category.controllers");

const router = express.Router();

router.get("/", getAllCategory);
router.post("/", addCategory);
router.get("/:id", getCategoryById);
router.get("/letter/:letter", getCategoryByLetter);
router.put("/:id", editCategory);
router.delete("/:id", deleteCategory);

module.exports = router;
