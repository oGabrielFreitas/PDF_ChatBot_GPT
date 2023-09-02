/* eslint-disable */

import {OpenAIEmbeddings} from 'langchain/embeddings/openai';

import {ChromaClient} from 'chromadb';


import {OpenAI} from 'langchain/llms/openai';

const llm = new OpenAI({
	openAIApiKey: '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',
    temperature: 0.9,
});

export const loadVectordb = async persistDir => {
	// const embeddings = new OpenAIEmbeddings({openaiApiKey: process.env.OPENAI_API_KEY});

	// return new ChromaClient({client: persistentClient, embeddingFunction: embeddings});

    const result = await llm.predict(persistDir);

    return result


};
