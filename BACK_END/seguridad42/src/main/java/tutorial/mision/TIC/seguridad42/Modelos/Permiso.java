package tutorial.mision.TIC.seguridad42.Modelos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.annotation.Id;

@Data
@Document()
@NoArgsConstructor
@AllArgsConstructor
@Slf4j
public class Permiso {
    @Id
    private String _id;
    private String url;
    private String metodo;

    public String get_id() {
        return _id;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getMetodo() {
        return metodo;
    }

    public void setMetodo(String metodo) {
        this.metodo = metodo;
    }

    @Override
    public String toString() {
        return "Permiso{" +
                "url='" + url + '\'' +
                ", metodo='" + metodo + '\'' +
                '}';
    }
}
