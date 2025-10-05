import { FiCloud, FiSun, FiWind, FiDroplet, FiAlertTriangle } from "react-icons/fi";
import type { Temp } from "../../types/temp";

export type CardProps = {
  props: Temp;
  // title: string;
  time: string;
  city: string;
  image: string;
  statusClima?: string;
  bgColor?: string;
};

export default function Card({
  props,
  // title,
  time,
  city,
  image,
  statusClima,
  bgColor = "bg-amber-300",
}: CardProps) {

  const getImageByStatus = () => {
    if (!statusClima) return image;
    if (statusClima.includes("Warm") || statusClima.includes("Pleasant")) return "./src/assets/sunny.svg";
    if (statusClima.includes("Cold")) return "./src/assets/cloudy.svg";
    if (statusClima.includes("ventoso")) return ".src/assets/cloudy.svg";
    if (!statusClima.includes("no chance of rain")) return ".src/assets/rain.svg";
    if (statusClima.includes("desconfortável")) return ".src/assets/cloudy.svg";
    return image;
  };

  return (
    <section className="*:box-border w-[240px] h-[320px] flex flex-col items-center justify-center text-center mt-4 p-3">
      <picture className={`w-full h-[40%] flex flex-col items-center gap-2 p-2 rounded-t-lg ${bgColor}`}>
        <img src={getImageByStatus()}  className="w-12 h-12" />
        {/* <p className="text-xl font-bold text-sky-950">{title}</p> */}
      </picture>
      <article className="w-full h-[60%] flex flex-col gap-2 rounded-b-lg font-bold pt-2 text-sky-950 bg-white">
        <h3 className="text-4xl">{props.temperatura}</h3>
        <div>
          <p className="text-sm">{time}</p>
          <p className="text-sm">{city}</p>
        </div>
        <div>
          <hr className="mb-2 text-gray-200" />
          <p className="text-xs">{props.chanceChuva}</p>
            {statusClima && (
              <p className="text-xs mt-1 flex items-center justify-center gap-1">
                {(statusClima.includes("Warm") || statusClima.includes("Pleasant")) && <FiSun className="inline text-yellow-500" />}
                {statusClima.includes("Cold") && <FiCloud className="inline text-blue-400" />}
                {statusClima.includes("ventoso") && <FiWind className="inline text-sky-500" />}
                {!statusClima.includes("no chance of rain") && <FiDroplet className="inline text-blue-600" />}
                {statusClima.includes("desconfortável") && <FiAlertTriangle className="inline text-red-500" />}
                {statusClima}
              </p>
            )}
        </div>
      </article>
    </section>
  );
}