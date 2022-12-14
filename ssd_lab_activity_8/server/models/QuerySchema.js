const mongoose = require("mongoose");

let Schema = mongoose.Schema;
const QuerySchema = new Schema(
  {
    rollNumber: {
      type: String,
      required: true,
    },
    password: {
      type: String,
      required: true,
    },
    role: {
      type: String,
      required: true,
    },
  },
  {
    timestamps: true,
  }
);

const Query = mongoose.model("Query", QuerySchema);

module.exports = Query;
