module.exports = {
    env: {
      browser: true,
      es2021: true,
    },
    extends: [
      'eslint:recommended',
      'plugin:security/recommended'
    ],
    plugins: ['security'],
    rules: {
      'security/detect-eval-with-expression': 'error'
    }
  }