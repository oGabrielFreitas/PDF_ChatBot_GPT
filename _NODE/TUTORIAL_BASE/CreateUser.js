"use strict";
// Criar nome, email e password
Object.defineProperty(exports, "__esModule", { value: true });
exports.createUserEstruturada = void 0;
function createUser({ name, email, password }) {
    const user = {
        name,
        email,
        password,
    };
    return user;
}
exports.default = createUser;
// Criar com os parâmetros separados ao invés de usar interface
function createUserEstruturada(name = '', email, password) {
    const user = {
        name,
        email,
        password,
    };
    return user;
}
exports.createUserEstruturada = createUserEstruturada;
