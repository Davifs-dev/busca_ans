<template>
  <div class="container">
    <div class="search-box">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Digite para buscar operadoras..."
        class="search-input"
      />
      <button @click="search" class="search-button">Buscar</button>
    </div>

    <div v-if="operadoras.length > 0" class="result-list">
      <div
        v-for="operadora in operadoras"
        :key="operadora.CNPJ"
        class="operadora-card"
      >
        <h3 class="operadora-title">
          {{ operadora.Nome_Fantasia || "Nome Fantasia não informado" }}
        </h3>
        <p><strong>Razão Social:</strong> {{ operadora.Razao_Social }}</p>
        <p><strong>Registro ANS:</strong> {{ operadora.Registro_ANS }}</p>
        <p><strong>CNPJ:</strong> {{ operadora.CNPJ }}</p>
        <p><strong>Modalidade:</strong> {{ operadora.Modalidade }}</p>

        <div class="section">
          <h4>📍 Endereço</h4>
          <p><strong>Logradouro:</strong> {{ operadora.Logradouro }}</p>
          <p><strong>Número:</strong> {{ operadora.Numero }}</p>
          <p>
            <strong>Complemento:</strong>
            {{ operadora.Complemento || "Não informado" }}
          </p>
          <p><strong>Bairro:</strong> {{ operadora.Bairro }}</p>
          <p>
            <strong>Cidade:</strong> {{ operadora.Cidade }} - {{ operadora.UF }}
          </p>
          <p><strong>CEP:</strong> {{ operadora.CEP }}</p>
        </div>

        <div class="section">
          <h4>📞 Contato</h4>
          <p>
            <strong>Telefone:</strong> ({{ operadora.DDD }})
            {{ operadora.Telefone }}
          </p>
          <p><strong>Fax:</strong> {{ operadora.Fax || "Não informado" }}</p>
          <p>
            <strong>E-mail:</strong>
            {{ operadora.Endereco_eletronico || "Não informado" }}
          </p>
        </div>

        <div class="section">
          <h4>👨‍💼 Representante</h4>
          <p><strong>Nome:</strong> {{ operadora.Representante }}</p>
          <p><strong>Cargo:</strong> {{ operadora.Cargo_Representante }}</p>
        </div>

        <p>
          <strong>Região de Comercialização:</strong>
          {{ operadora.Regiao_de_Comercializacao }}
        </p>
        <p>
          <strong>Data de Registro ANS:</strong>
          {{ operadora.Data_Registro_ANS }}
        </p>
      </div>
    </div>

    <p v-if="searched && operadoras.length === 0" class="no-results">
      Nenhuma operadora encontrada.
    </p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchQuery: "",
      operadoras: [],
      searched: false,
    };
  },
  methods: {
    async search() {
      this.searched = true; // Marca que a pesquisa foi feita
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/operadoras/buscar/?query=${this.searchQuery}`
        );
        this.operadoras = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.search-box {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}

.result-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.operadora-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
}

.operadora-title {
  font-size: 18px;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 5px;
}

.sub-info {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.section {
  margin-top: 10px;
  padding: 8px;
  background-color: #eef4ff;
  border-radius: 5px;
}

.section h4 {
  margin: 0;
  font-size: 16px;
  color: #333;
}

.no-results {
  text-align: center;
  color: #888;
}
</style>
