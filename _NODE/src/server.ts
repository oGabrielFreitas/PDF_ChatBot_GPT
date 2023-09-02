/* eslint-disable */

import express from 'express';
import routes from './routes';

// Import {loadVectordb} from './bot_functions';

const app = express();

const API_KEY = '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'

// ---------------------------------------

import {OpenAIEmbeddings} from 'langchain/embeddings/openai';

import {ChromaClient} from 'chromadb';

import {OpenAI} from 'langchain/llms/openai';

// Load LLM
const llm = new OpenAI({
	openAIApiKey: API_KEY,
});

// Load VectorDB
const loadVectordb = async (persistDir: string) => {
// Const embeddings = new OpenAIEmbeddings({openaiApiKey: process.env.OPENAI_API_KEY});

// return new ChromaClient({client: persistentClient, embeddingFunction: embeddings});

	llm.predict(persistDir);

    return true;
};

import {Chroma} from 'langchain/vectorstores/chroma'


const easy_answer = async (query: string) => {

    const embeddings = new OpenAIEmbeddings({
        openAIApiKey: API_KEY, // In Node.js defaults to process.env.OPENAI_API_KEY
        batchSize: 512, // Default value if omitted is 512. Max is 2048
      });

      // Create docs with a loader
    const loader = new TextLoader("src/example.txt");
    const docs = await loader.load();

    // Create vector store and index the docs
    const vectorStore = await Chroma.fromDocuments(docs, new OpenAIEmbeddings({
        openAIApiKey: API_KEY, // In Node.js defaults to process.env.OPENAI_API_KEY
        batchSize: 512, // Default value if omitted is 512. Max is 2048
      }), {
    collectionName: "a-test-collection",
    url: "http://localhost:8000", // Optional, will default to this value
    collectionMetadata: {
        "hnsw:space": "cosine",
    }, // Optional, can be used to specify the distance method of the embedding space https://docs.trychroma.com/usage-guide#changing-the-distance-function
    });

    // Search for the most similar document
    const response = await vectorStore.similaritySearch("hello", 1);

    console.log('RESPONSE:')
    console.log(response)

}





import { Chroma } from "langchain/vectorstores/chroma";
import { OpenAIEmbeddings } from "langchain/embeddings/openai";
import { TextLoader } from "langchain/document_loaders/fs/text";




































app.get('/', (request, response) => response.json({message: 'Hello World'}));

app.get('/teste', async (request, response) => {
	const resp = await loadVectordb('Qual a capital do Brasil?');
	response.json({message: resp});
});

app.get('/teste2', async (request, response) => {
	const resp = await easy_answer('olá');
	response.json({message: resp});
});


app.listen(3333, () => {
	console.log('🚀 Server stated on port 3333!');
});
