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
    user_is_creator: {
      type: Boolean,
    },
    created_data: {
      type: String,
      trim: true,
    },
    updated_at: {
      type: String,
      trim: true,
    },
    user_token: {
      type: String,
    },
    user_activation_link: {
      type: String,
    },
    user_is_active: {
      type: Boolean,
      default: false,
    },
  },
  { versionKey: false }
);

module.exports = model("User", userSchema);
