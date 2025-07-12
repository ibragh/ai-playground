#!/bin/bash
# Simple script to stop the API container if no connections for a period of time
IDLE_THRESHOLD=${IDLE_THRESHOLD:-300}  # 5 minutes
CONTAINER_NAME=${CONTAINER_NAME:-mcp-ai-agent-api-1}
LAST_ACTIVITY=$(docker inspect --format='{{.State.StartedAt}}' $CONTAINER_NAME)
while true; do
  NOW=$(date +%s)
  LAST=$(date --date="$LAST_ACTIVITY" +%s)
  DIFF=$((NOW-LAST))
  if [ $DIFF -gt $IDLE_THRESHOLD ]; then
    echo "Stopping container $CONTAINER_NAME due to inactivity"
    docker stop $CONTAINER_NAME
    exit 0
  fi
  sleep 60
done
