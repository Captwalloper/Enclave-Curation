# Untitled Stellaris Mod (probably Enclave stuff)

## Steam Workshop Mod for Stellaris

[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://steamcommunity.com/workshop/filedetails/)

---

## Description

**Enclave Overhaul** extends the existing enclave system, enabling players to add, move, and remove enclaves from their systems in a balanced, lore friendly way. Just like Grand Archive allows players to interact with and curate wild space wildlife, Enclave curation empowers players to  collect and manage enclaves.

---

## Major Features

### 🎭 Invite/Evict Enclaves

- Invite enclaves to establish an outpost in your systems, exactly where you choose via the enclave outpost site megastructure. They have some fleet power, so have fun with chokepoints!
- Evict enclaves you've invited, in case you want to move them or roleplay.

### 🏛️ New Starbase Building

- **Enclave Trading Company** -- Invite at least 1 enclave into a system to start trading. Provides 10 trade value for each enclave invited, and not evicted. If an enclave blows up, trade with its remnants.

---

## Compatibility

- **Stellaris 4.3.3** or later should work, earlier is untested
- Compatible with most other mods; only additions were made.

---

## Installation

### Via Steam Workshop

1. Open [Steam](https://steamcommunity.com/workshop/browse/?appid=281990)
2. Navigate to the mod page for "Enclave Curation"
3. Click **Subscribe**
4. Launch Stellaris to automatically download
5. Enjoy the enhanced enclave experience!

### Manual Installation (Advanced Users)

1. Download the mod from Steam Workshop
2. Extract the `mod` folder
3. Copy the `mod` folder to your `Documents\Paradox Interactive\Stellaris\mods` folder
4. Launch Stellaris and enable the mod in Options → Mods → Enclave Curation

---

## Dev

Mainly writing this for future me...
I wrote some auxillary scripts to aid development.

1. Ensure python is installed (via choco->pyenv or just windows store)
2. In commandline, run `pip install -r requirements.txt` (or just `invoke restore` after this)
3. `inv --list` (`inv` is shorter alias for invoke)

And ya, I deliberately committed a zip of the mod. My mercy for any goofy goobers who somehow find the git page and can't figure out how to download the repo xD.
