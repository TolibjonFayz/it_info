const { Schema, model } = require("mongoose");

const adminSchema = new Schema(
  {
    admin_name: {
      type: String,
      trim: true,
      required: true,
    },
    admin_email: {
      type: String,
      required: true,
      unique: true,
    },
    admin_password: {
      type: String,
      required: true,
    },
    admin_is_active: {
      type: Boolean,
    },
    admin_is_creator: {
      type: Boolean,
    },
    created_data: {
      type: String,
    },
    updated_at: {
      type: String,
    },
  },
  { versionKey: false }
);

module.exports = model("Admin", adminSchema);
