const { Command } = require('discord-akairo');
const constants = require('../constants');
const db = require('../util/database');

class LeaderboardCommand extends Command {
  constructor() {
    super('leaderboard', {
      aliases: constants.leaderboardAliases,
      channel: 'guild',
    });
  }

  exec(message) {
    console.log(`Leaderboard requested by ${message.author.tag}`);
    message.guild.members.fetch().then(() => {
      const guildMembers = message.guild.members.cache.array();
      var userMap = {};
      for (let guildMember of guildMembers) {
        const user = guildMember.user;
        userMap[user.id] = user.username;
      }
      db.getLeaderboard(userMap, message, displayLeaderboard);
    });
  }
}

function displayLeaderboard(data, userMap, message) {
  var scores = [];
  for (let item of data.Items) {
    if (!(item.UserId in userMap)) {
      continue;
    }
    var curScoreObject = new ScoreObject(
      item.UserId,
      userMap[item.UserId],
      item.Score
    );
    scores.push(curScoreObject);
  }
  scores.sort((a, b) => {
    return b.score - a.score;
  });
  var msg = '**Here are the top scores on this server:**\n```\n';
  msg += '+------------------------------------------+\n';
  for (var i = 0; i < 10 && i < scores.length; i++) {
    if (scores[i].score <= 0) {
      break;
    }
    var rank = i + 1;
    msg += `| ${(rank + '.').padEnd(4)}${scores[i].username.padEnd(23)}${
      ('$' + scores[i].score.toLocaleString()).padStart(13) + ' |\n'
    }`;
  }
  msg += '+------------------------------------------+\n';
  msg += '```';
  message.channel.send(msg);
}

function ScoreObject(userId, username, score) {
  this.userId = userId;
  this.username = username;
  this.score = score;
}

module.exports = LeaderboardCommand;
