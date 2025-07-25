import js from "@eslint/js";
import pluginSecurity from "eslint-plugin-security";

/** @type {import("eslint").Linter.FlatConfig[]} */
export default [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    plugins: {
      security: pluginSecurity
    },
    rules: {
      "security/detect-eval-with-expression": "error"
    }
  }
];