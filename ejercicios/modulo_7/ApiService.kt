import retrofit2.http.GET
import retrofit2.http.Path

// Interface de Retrofit para la API de JSONPlaceholder
interface ApiService {
    // Endpoint para obtener un usuario por ID
    @GET("users/{userId}")
    suspend fun getUserById(@Path("userId") userId: Int): User
}