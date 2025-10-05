import { FiCloud, FiSun, FiWind, FiDroplet, FiAlertTriangle } from "react-icons/fi";
import type { Temp } from "../../types/temp";

const weatherDefitinitionRules = [
  { 
    rule: (evento: string) => evento.includes("Warm") || evento.includes("Pleasant"),
    color: "bg-amber-300",
    image: "./src/assets/sunny.svg",
    icon: <FiSun className="inline text-yellow-500" /> 
  },
  { 
    rule: (evento: string) => evento.includes("Cold"),
    color: "bg-blue-300",
    image: "./src/assets/cloudy.svg",
    icon: <FiCloud className="inline text-blue-400" />
  },
  { 
    rule: (evento: string) => evento.includes("ventoso"),
    color: "bg-sky-300",
    image: "./src/assets/cloudy.svg",
    icon: <FiWind className="inline text-sky-400" />
  },
  { 
    rule: (evento: string) => !evento.includes("no chance of rain"),
    color: "bg-indigo-300",
    image: "./src/assets/rain.svg",
    icon: <FiDroplet className="inline text-indigo-400" />
  },
  { 
    rule: (evento: string) => evento.includes("desconfortável"),
    color: "bg-rose-300",
    image: "./src/assets/cloudy.svg",
    icon: <FiAlertTriangle className="inline text-rose-400" />
  }
]

export type CardProps = {
  props: Temp;
};

export default function Card({
  props,
}: CardProps) {

  const getImageByStatus = () => {
    let image = "./src/assets/sunny.svg";
    weatherDefitinitionRules.forEach(def => {
      if (def.rule(props.evento)) {
        image = def.image;
      }
    });
    return image;
  };

  const getBackgroundColorByStatus = () => {
    let color = "bg-amber-300";
    weatherDefitinitionRules.forEach(def => {
      if (def.rule(props.evento)) {
        color = def.color;
      }
    });
    return color;
  };

  const getIconByStatus = () => {
    let icon = <FiSun className="inline text-yellow-500" />;
    weatherDefitinitionRules.forEach(def => {
      if (def.rule(props.evento)) {
        icon = def.icon;
      }
    });
    return icon;
  };

  const getFormattedDate = (dateString: string) => {
    const date = new Date(dateString);
    const dateISO = date.toISOString();
    const dateStringFormatted = dateISO.substring(8, 10) + "/" + dateISO.substring(5, 7) + "/" + dateISO.substring(0, 4) + " - " + dateISO.substring(11, 16);
    return dateStringFormatted;
  }

  return (
    !props.error ? (
    <section className="*:box-border w-full h-[320px] flex flex-col items-center justify-center text-center p-3">
      <picture className={`w-full h-[40%] flex items-center justify-center rounded-t-lg ${getBackgroundColorByStatus()}`}>
        <img src={getImageByStatus()}  className="w-12 h-12" />
        {/* <p className="text-xl font-bold text-sky-950">{title}</p> */}
      </picture>
      <article className="w-full h-[60%] flex flex-col gap-2 rounded-b-lg font-bold pt-2 text-sky-950 bg-white">
        <h3 className="text-4xl">{Math.trunc(parseFloat(props.temperatura))}ºC</h3>
        <div>
          <p className="text-sm">{getFormattedDate(props.dataEHora)}</p>
          <p className="text-sm">{props.localidade}</p>
        </div>
        <div>
          <hr className="mb-2 text-gray-200" />
          <p className="text-xs">Rain probability: {props.chanceChuva}%</p>
            {props.evento && (
              <p className="text-xs mt-1 flex items-center justify-center gap-1">
                {getIconByStatus()}
                {props.evento}
              </p>
            )}
        </div>
      </article>
    </section>
  ) : props.mensagem);
}