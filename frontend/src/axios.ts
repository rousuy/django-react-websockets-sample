import axios from "axios";
import config from "config/index";
import { useNavigate } from "react-router-dom";


const useAxiosWithInterceptor = () => {
  const jwtAxios = axios().create({
    baseURL: config.BASE_URL,
    timeout: config.API_TIMEOUT_MILLISECONDS,
    headers: {
      'Content-Type': 'application/json',
      accept: 'application/json',
    },
  })
  const navigate = useNavigate()
  
  jwtAxios.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      const originalRequest = error.config;
      if (error.response?.status === 403) {
        const goRoot = () => navigate("/")
        goRoot();
      }
  }
  )
  return jwtAxios;
}
export default useAxiosWithInterceptor;







