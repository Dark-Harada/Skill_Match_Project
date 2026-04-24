const API = "http://127.0.0.1:8000";

async function loadPlayers() {
    const res = await fetch(`${API}/players`);
    const players = await res.json();

    const container = document.getElementById("players");
    container.innerHTML = "";

    players.forEach(p => {
        container.innerHTML += `
            <div class="player">
                <span>${p.name}</span>
                <span>${p.rank} (${p.winrate}%)</span>
            </div>
        `;
    });
}

async function findMatch() {
    const res = await fetch(`${API}/matchmaking/1`);
    const team = await res.json();

    const container = document.getElementById("team");
    container.innerHTML = "";

    team.forEach(p => {
        container.innerHTML += `
            <div class="player">
                <span>${p.name}</span>
                <span>${p.rank}</span>
            </div>
        `;
    });
}

loadPlayers();