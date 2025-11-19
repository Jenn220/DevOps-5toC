# Usar la imagen oficial de Node.js como base
FROM node:18-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de definición de dependencias
COPY package*.json ./

# Instalar las dependencias
RUN npm ci --only=production

# Copiar el código fuente
COPY . .

# Exponer el puerto que usa la aplicación (ajustado al puerto correcto)
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "src/index.js"]