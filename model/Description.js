const { Schema, model } = require("mongoose");

const descriptionScheme = new Schema(
  {
    description: {
      type: String,
      required: true,
      trim: true,
    },
    category_id: {
      type: Schema.Types.ObjectId,
      ref: "Category",
    },
  },
  {
    versionKey: false,
  }
);

module.exports = model("Description", descriptionScheme);
