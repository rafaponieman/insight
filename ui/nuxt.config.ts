// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@formkit/nuxt',
    '@pinia/nuxt',
    '@nuxtjs/google-fonts',
    '@nuxtjs/tailwindcss'
  ],
  googleFonts: {
    families: {
      Lato: [100, 300, 400, 500, 600, 700],
    }
  },
  formkit: {
    // Experimental support for auto loading
    autoImport: true
  },
  runtimeConfig: {
    public: {
      apiRoot: ''
    }
  }
})
