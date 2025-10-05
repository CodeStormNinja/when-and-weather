package CodeStormNinja.back_end_parade.service;

import CodeStormNinja.back_end_parade.model.ClimaInput;
import CodeStormNinja.back_end_parade.model.ClimaOutput;
import CodeStormNinja.back_end_parade.model.DadosBrutos;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;


@Service
public class ClimaService {

    private final RestTemplate restTemplate;
    private final String apiDadosBaseUrl;
    private final Logger logger = LoggerFactory.getLogger(ClimaService.class);

    public ClimaService(@Value("${api.dados.base-url}") String apiDadosBaseUrl) {
        this.restTemplate = new RestTemplate();
        this.apiDadosBaseUrl = apiDadosBaseUrl;
    }


    public ClimaOutput analisarStatus(ClimaInput input) {

        try {
            DadosBrutos dadosBrutos = buscarDadosBrutosSimulados(input);
            String statusClima = logicaNegocio(dadosBrutos);
            return new ClimaOutput(statusClima, dadosBrutos.getTemperatura(), dadosBrutos.getChancePrecipitacao());
        
        } catch (Exception e) {
            logger.error("An error occurred during climate analysis: ", e);
            throw e;
        }
    }

    public DadosBrutos buscarDadosBrutosSimulados(ClimaInput input) {
        String endpoint = "/weather-forecast";

        String url = apiDadosBaseUrl + endpoint;

        logger.info("Fetching data from URL: " + url + " using POST method.");

        try {
            DadosBrutos dados = restTemplate.postForObject(url, input, DadosBrutos.class);

            return dados;

        } catch (Exception e) {
            logger.error("Error calling Data API (" + url + "): " + e.getMessage());
            throw e;
        }
    }

    public String logicaNegocio(DadosBrutos dados) {
        String statusTemperatura;
        double temp = dados.getTemperatura();
        double umidade = dados.getChancePrecipitacao();

        if (temp >= 0 && temp <= 9) {
            statusTemperatura = "Very Cold";
        } else if (temp > 9 && temp <= 15) {
            statusTemperatura = "Cold";
        } else if (temp > 15 && temp <= 24) {
            statusTemperatura = "Pleasant";
        } else if (temp > 24 && temp <= 29) {
            statusTemperatura = "Warm";
        } else if (temp > 29 && temp < 36) {
            statusTemperatura = "Very Warm";
        } else if (temp >= 36) {
            statusTemperatura = "Extremely Warm";
        } else {
            statusTemperatura = "Invalid Data";
        }


        if (umidade > 70) {
            return statusTemperatura + " with high chance of rain.";
        } else if (umidade > 40) {
            return statusTemperatura + " with low chance of rain.";
        } else {
            return statusTemperatura + " with no chance of rain.";

        }

    }
}