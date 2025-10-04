package CodeStormNinja.back_end_parade.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class DadosBrutos {
    @JsonProperty("temperature_2m")
    private double temperatura;
    @JsonProperty("rain")
    private double valorPrecipitacao;
    @JsonProperty("precipitation_probability")
    private double chancePrecipitacao;
    @JsonProperty("wind_gusts_10m")
    private double velocidadeRajadasVento;
    @JsonProperty("snowfall")
    private double valorIntensidadeNeve;

    public DadosBrutos() {
    }

    public DadosBrutos(double temperatura, double valorPrecipitacao, double chancePrecipitacao, double velocidadeRajadasVento, double valorIntensidadeNeve) {
        this.temperatura = temperatura;
        this.valorPrecipitacao = valorPrecipitacao;
        this.chancePrecipitacao = chancePrecipitacao;
        this.velocidadeRajadasVento = velocidadeRajadasVento;
        this.valorIntensidadeNeve = valorIntensidadeNeve;
    }

    public DadosBrutos(double temperatura, double valorPrecipitacao, double chancePrecipitacao) {
        this.temperatura = temperatura;
        this.valorPrecipitacao = valorPrecipitacao;
        this.chancePrecipitacao = chancePrecipitacao;
    }

    public double getTemperatura() {
        return temperatura;
    }

    public void setTemperatura(double temperatura) {
        this.temperatura = temperatura;
    }

    public double getValorPrecipitacao() {
        return valorPrecipitacao;
    }

    public void setValorPrecipitacao(double valorPrecipitacao) {
        this.valorPrecipitacao = valorPrecipitacao;
    }

    public double getChancePrecipitacao() {
        return chancePrecipitacao;
    }

    public void setChancePrecipitacao(double chancePrecipitacao) {
        this.chancePrecipitacao = chancePrecipitacao;
    }

    public double getVelocidadeRajadasVento() {
        return velocidadeRajadasVento;
    }

    public void setVelocidadeRajadasVento(double velocidadeRajadasVento) {
        this.velocidadeRajadasVento = velocidadeRajadasVento;
    }

    public double getValorIntensidadeNeve() {
        return valorIntensidadeNeve;
    }

    public void setValorIntensidadeNeve(double valorIntensidadeNeve) {
        this.valorIntensidadeNeve = valorIntensidadeNeve;
    }
}


