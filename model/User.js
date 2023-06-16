const { Schema, model } = require("mongoose");

const userSchema = new Schema(
  {
    user_name: {
      type: String,
      trim: true,
    },
    user_email: {
      type: String,
      trim: true,
    },
    user_password: {
      type: String,
    },
    admin_is_active: {
      type: Boolean,
    },
    admin_is_creator: {
      type: Boolean,
    },
    created_data: {
      typel: String,
      trim: true,
    },
    updated_at: {
      type: String,
      trim: true,
    },
  },
  { versionKey: false }
);

module.exports = model("User", userSchema);
