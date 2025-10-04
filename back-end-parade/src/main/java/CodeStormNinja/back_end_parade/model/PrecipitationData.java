package CodeStormNinja.back_end_parade.model;

public class PrecipitationData {


    private float valorPrecipitacao;
    private float chancePrecipitacao;
    private float probabilidadeRaios;

    public PrecipitationData(float valorPrecipitacao, float chancePrecipitacao, float probabilidadeRaios) {
        this.valorPrecipitacao = valorPrecipitacao;
        this.chancePrecipitacao = chancePrecipitacao;
        this.probabilidadeRaios = probabilidadeRaios;
    }

    public float getValorPrecipitacao() {
        return valorPrecipitacao;
    }

}