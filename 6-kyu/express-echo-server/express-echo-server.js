const express = require("express");
const app = express(); // be sure to use the variable `app`
app.use(express.json());
function process(message, res) {
    if (message === undefined) {
        return res.status(422).json({ error: "'message' was not provided" });
    }
    if (typeof message !== "string") {
        return res.status(422).json({ error: "'message' was not a string" });
    }
    res.status(200).json({ message });
}
app.get("/", (req, res) => process(req.query.message, res));
app.post("/", (req, res) => process(req.body.message, res));