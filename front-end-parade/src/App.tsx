import fundo from "./assets/background/background.png";
import { FiMapPin, FiCalendar } from "react-icons/fi";
import { FiCloud } from "react-icons/fi";
import Card from "./components/Card";
import type { Temp } from "./types/temp";
import { useState } from "react";
import { getTemp } from "./services/tempRequests.ts";
import Loading from "./components/Loading";

export function App() {
  const [temp, setTemp] = useState<Array<Temp>>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [localidade, setLocalidade] = useState<string>("");
  const [dataHora, setDataHora] = useState<string>("");

  async function getAllTemp() {
    setIsLoading(true);
    const response = await getTemp(localidade, dataHora);
    setIsLoading(false);
    if (response.success){
      response.data["dataEHora"] = dataHora;
      response.data["localidade"] = localidade;
      response.data["error"] = false;
      setTemp([response.data]);
    }
    else setTemp([{
      evento: "",
      mensagem: "Oops! Something went wrong, please try again. :(",
      dataEHora: "",
      localidade: "",
      temperatura: "",
      chanceChuva: "",
      error: true
    }]);
  }

  return (
    <div
      className="min-h-screen w-full bg-cover bg-center flex items-center justify-center px-2 md:px-0"
      style={{ backgroundImage: `url(${fundo})` }}
    >
      <div className="w-full max-w-3xl min-h-[400px] rounded-2xl bg-[#0b3773] shadow-2xl text-white text-sm md:text-base p-3 md:p-6 flex flex-col justify-between">
        <div className="w-full h-full flex flex-col justify-between gap-6 md:gap-8">
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between mb-0 md:mb-1 gap-1 md:gap-0">
            <div className="flex items-center gap-2 md:gap-3">
              <FiCloud className="text-2xl md:text-3xl text-white" />
              <h1 className="text-lg md:text-xl font-bold">
                When & Weather
              </h1>
            </div>
            <div className="flex gap-3 md:gap-4 text-xs md:text-base">
              <a href="#" className="hover:underline">
                About us
              </a>
              <a href="#" className="hover:underline">
                Contacts
              </a>
            </div>
          </div>

          {/* Barra de busca */}
          <div className="flex flex-col md:flex-row gap-1 md:gap-2 mb-0 md:mb-1 items-center w-full">
            <div className="relative w-full md:w-[260px]">
              <FiMapPin className="absolute left-2 top-1/2 -translate-y-1/2 text-blue-300 text-lg pointer-events-none" />
              <input
                onChange={(e) => setLocalidade(e.target.value)}
                type="text"
                placeholder="Local"
                className="pl-8 pr-2 py-2 rounded-md w-full text-xs md:text-sm border border-blue-300 bg-blue-900/40 text-white placeholder:text-blue-200 shadow-md focus:border-blue-400 focus:ring-2 focus:ring-blue-400 outline-none transition-all"
              />
            </div>
            <div className="relative w-full md:w-[180px]">
              <FiCalendar className="absolute left-2 top-1/2 -translate-y-1/2 text-blue-300 text-lg pointer-events-none" />
              <input
                onChange={(e) => setDataHora(e.target.value)}
                type="datetime-local"
                className="pl-8 pr-2 py-2 rounded-md w-full text-xs md:text-sm border border-blue-300 bg-blue-900/40 text-white placeholder:text-blue-200 shadow-md focus:border-blue-400 focus:ring-2 focus:ring-blue-400 outline-none transition-all hide-native-calendar"
              />
            </div>
            <button
              className="bg-gradient-to-r from-blue-500 to-blue-700 px-4 py-2 rounded-md font-bold text-xs md:text-sm shadow-md hover:from-blue-600 hover:to-blue-800 w-full md:w-auto transition-all"
              onClick={getAllTemp}
            >
              Get Forecast
            </button>
          </div>

          {/* Cards de previsão */}
          {isLoading ? (
            <Loading />
          ) : (
            <div className="flex md:flex-row justify-center min-h-[120px] md:min-h-[180px] w-full">
              {/* Cards de previsão */}
              {temp.map((card, idx) => <Card key={idx} props={card} />)}
            </div>
          )}
          {/* Rodapé */}
          <div className="flex flex-col md:flex-row justify-between text-xs md:text-sm text-gray-300 mt-4 gap-2 md:gap-0 w-full">
            <div>
              <span className="font-bold">When & Weather</span>
              <br />
              Providing you with personalized predictions and weather information for your needs.
            </div>
            <div>
              <span className="font-bold">Links</span>
              <br />
              About us | Contact
            </div>
            <div>
              <span className="font-bold">Credits</span>
              <br />
              Developed by CodeStormNinja
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
