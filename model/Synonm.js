const { Schema, model } = require("mongoose");

const SynonymScheme = new Schema(
  {
    desc_id: {
      type: Schema.Types.ObjectId,
      ref: "Description",
    },
    dict_id: {
      type: Schema.Types.ObjectId,
      ref: "Dictionary",
    },
  },
  { versionKey: false }
);

module.exports = model("Synonym", SynonymScheme);
