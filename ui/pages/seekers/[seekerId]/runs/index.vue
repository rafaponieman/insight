<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <section-header title="Runs">
      <NuxtLink
        to="/seekers/1/runs/add"
        type="button"
        class="text-white bg-gradient-to-r from-purple-500 via-purple-600 to-purple-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-purple-300 dark:focus:ring-purple-800 shadow-lg shadow-purple-500/50 dark:shadow-lg dark:shadow-purple-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
        data-modal-toggle="initiateRunModal" 
        data-modal-target="initiateRunModal"
      >
        Initiate run
      </NuxtLink>
    </section-header>
    <listing
      :columns="columns"
      :data="listingData"
      :additional="additional"
    >
      <template v-slot:custom-column>
        <div>pepe</div>
      </template>
    </listing>
  </section>
</template>

<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()

  const seekerId = route.params.seekerId

  const { data: listingData } = await useFetch(`${config.public.apiRoot}/runs/?seeker=${seekerId}`)
  console.log(listingData)

  const columns = [
    { name: 'id', label: 'ID' },
    { name : 'status', label: 'Status'},
    { name : 'start', label: 'Start'},
    { name : 'end', label: 'End'},
    { name: 'created', label: 'Created', type: 'date' }
  ]

  const additional = [
    { label: '3', linkData: (seeker) => ({ to: `/seekers/${seeker.id}/runs`, label: 'View runs'}) }
  ]
</script>
