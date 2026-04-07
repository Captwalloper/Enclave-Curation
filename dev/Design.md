# Design

## Features

### Fundamental Enclave Mechanics

<!-- * From enclave dialogue, gain cap/permission? to build branch for that kind of enclave
* For cheap influence, move enclave within same system
* For mild influence, move enclave between your owned systems
* For big influence, remove enclave... or just declare hostilities and blow it up (relationship malice if faction survives)
* Salvation event if above configurable relation with enclave -->
* branch
* move -- same system
* move -- different owned system
* demolish -- resettle (10k energy, 250 influence), or fight (station becomes hostile)
* salvation event -- within n days pay price/research special project to claim endangered enclave

### Other stuff

* Room for potential expansion
* Compatibility with other mods
* credit to predecessor mods
* localization

## Implementation

* Megastructure ghost
  * on-complete triggers swap with ship entity
* Scripted Effect
  * swap megastructure ghost with enclave

### TODO

* Parameterize for difference enclaves
* Resurection
* Pre-reqs for building enclaves
* Move & Remove
* DLC checks [Enclave DLC Reference](https://stellaris.paradoxwikis.com/Enclaves)
