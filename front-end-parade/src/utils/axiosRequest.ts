import instance from '../configAxios.ts';

function handleError(error: any) {
  return {
    success: false,
    tipo: 'error',
    data: error.response.data.status_message || 'Erro ao realizar operação',
  };
}

export const postRequest = async (url: string, obj: any) => {
  const axios = instance();

  try {
    const response = await axios.post(url, obj);
    return {
      data: response.data,
      success: true,
    };
  } catch (error: any) {
    return handleError(error);
  }
};

export const getRequest = async (url: string) => {
  const axios = instance();
  try {
    const response = await axios.get(url);
    return { data: response.data, success: true };
  } catch (error: any) {
    return handleError(error);
  }
};