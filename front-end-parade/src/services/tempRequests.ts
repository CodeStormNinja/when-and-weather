import { getRequest } from "../utils/axiosRequest.ts";

export const getTemp = async (localidade: string, dataHora: string) => {
  // http://localhost:8080/api/clima/analise?localidade=Sobral&dataEHora=2025-09-17T10:30:00
  return await getRequest(`clima/analise?localidade=${localidade}&dataEHora=${dataHora}`)
    .catch((error) => {
      return { success: false, data: error };
    });
};