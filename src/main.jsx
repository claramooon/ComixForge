import React from “react”;
import ReactDOM from “react-dom/client”;

function App() {
const [count, setCount] = React.useState(0);
return React.createElement(“div”,
{ style: { background: “red”, color: “white”, padding: 40, fontSize: 24, fontFamily: “sans-serif” } },
“COMIX FORGE IS ALIVE! Count: “ + count + “ “,
React.createElement(“button”,
{ onClick: function() { setCount(count + 1); }, style: { fontSize: 20, marginLeft: 10 } },
“Click me”
)
);
}

ReactDOM.createRoot(document.getElementById(“root”)).render(React.createElement(App));
