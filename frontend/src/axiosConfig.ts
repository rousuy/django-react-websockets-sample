import axios, { AxiosInstance } from "axios";
import config from "config/index";
import { useNavigate } from "react-router-dom";

const useAxiosWithInterceptor = (): AxiosInstance => {
  const jwtAxios = axios.create({ baseURL: config.BASE_URL });
  const navigate = useNavigate();

  jwtAxios.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      const originalRequest = error.config;
      if (error.response?.status === 403) {
        const goRoot = () => navigate("/");
        goRoot();
      }
      throw error;
    }
  );

  return jwtAxios;
};

export default useAxiosWithInterceptor;




