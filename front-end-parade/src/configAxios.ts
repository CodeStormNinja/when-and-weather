import axios from 'axios';
import type { AxiosInstance } from 'axios';
import { API_URL } from './constants/apiUrl.ts';

const getAxios = (timeout: number = 600000) => {
  const instance: AxiosInstance = axios.create({
    baseURL: API_URL,
    timeout: timeout,
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    },
  });

  return instance;
};

export default getAxios;