const express = require("express");
const config = require("config");
const mongoose = require("mongoose");

const PORT = config.get("port") || 3030;

const app = express();

//Barcha routlarni chaqirdik
const mainRouter = require("./routes/index.routes");

app.use(express.json());

//barcha routlarga yo`l
app.use(mainRouter);

//Daatbazaga ulanib serverni ishga tushirish
async function start() {
  try {
    await mongoose.connect(config.get("atlasURI"));

    app.listen(PORT, () => {
      console.log(`Server ${PORT}-portda ishga tushdi!`);
    });
  } catch (error) {
    console.log("Serverda xatolik");
  }
}

start();
