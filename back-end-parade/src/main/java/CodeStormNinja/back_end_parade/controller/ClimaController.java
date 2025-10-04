package CodeStormNinja.back_end_parade.controller;

import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import CodeStormNinja.back_end_parade.model.ClimaInput;
import CodeStormNinja.back_end_parade.model.ClimaOutput;
import CodeStormNinja.back_end_parade.service.ClimaService;

@RestController
@RequestMapping("/api/clima")
public class ClimaController {

  private ClimaService climaService;

  public ClimaController(ClimaService climaService) {
    this.climaService = climaService;
  }

  @GetMapping("/analise")
  ResponseEntity<ClimaOutput> analiseClima(
      @RequestParam String localidade,
      @RequestParam LocalDateTime dataEHora) {

    try {
      ClimaInput input = new ClimaInput(localidade, dataEHora);
      ClimaOutput output = climaService.analisarStatus(input);
      return ResponseEntity.ok(output);
    } catch (Exception e) {
      System.err.println("error when analyzing climate" + e.getMessage());
      return ResponseEntity.internalServerError().body(null);
    }
  }
}
