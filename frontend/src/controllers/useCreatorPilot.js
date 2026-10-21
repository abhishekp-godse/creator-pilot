/**
 * CreatorPilot - Frontend Controller (Custom Hook)
 * Decouples business logic, API requests, and state management from View components.
 */

import { useState, useEffect } from 'react';
import axios from 'axios';

export function useCreatorPilot() {
  const [summary, setSummary] = useState(null);
  const [notifications, setNotifications] = useState([]);
  const [forecast, setForecast] = useState(null);
  const [gaps, setGaps] = useState([]);
  const [videos, setVideos] = useState([]);
  const [trends, setTrends] = useState([]);
  const [ideas, setIdeas] = useState([]);
  const [collabs, setCollabs] = useState([]);
  const [loading, setLoading] = useState(true);

  // Modals state
  const [coachOpen, setCoachOpen] = useState(false);
  const [titleScorerOpen, setTitleScorerOpen] = useState(false);
  const [initialScorerTitle, setInitialScorerTitle] = useState('');
  const [weeklyPlanOpen, setWeeklyPlanOpen] = useState(false);

  const loadAllData = async () => {
    setLoading(true);
    try {
      const [sumRes, notifRes, foreRes, gapsRes, vidRes, trendsRes, ideasRes, collabsRes] =
        await Promise.all([
          axios.get('/api/channel/summary'),
          axios.get('/api/channel/notifications'),
          axios.get('/api/ml/growth-forecast'),
          axios.get('/api/growth/content-gaps'),
          axios.get('/api/channel/videos'),
          axios.get('/api/trends/niche'),
          axios.get('/api/growth/idea-vault'),
          axios.get('/api/growth/collab-matcher'),
        ]);

      setSummary(sumRes.data);
      setNotifications(notifRes.data);
      setForecast(foreRes.data);
      setGaps(gapsRes.data);
      setVideos(vidRes.data);
      setTrends(trendsRes.data);
      setIdeas(ideasRes.data);
      setCollabs(collabsRes.data);
    } catch (err) {
      console.warn('Backend not reached on /api, using client demo state:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAllData();
  }, []);

  const addIdea = async (title, source = 'user', effort = 'Medium (3-5h)') => {
    try {
      const res = await axios.post('/api/growth/idea-vault', { title, source, effort });
      setIdeas((prev) => [res.data, ...prev]);
    } catch (err) {
      // Fallback optimistic update
      const newItem = {
        id: `idea_${Date.now()}`,
        title,
        source,
        predicted_score: 88,
        production_effort: effort,
        tags: ['custom'],
        status: 'vault',
      };
      setIdeas((prev) => [newItem, ...prev]);
    }
  };

  const openTitleScorerWith = (title) => {
    setInitialScorerTitle(title);
    setTitleScorerOpen(true);
  };

  return {
    state: {
      summary,
      notifications,
      forecast,
      gaps,
      videos,
      trends,
      ideas,
      collabs,
      loading,
      coachOpen,
      titleScorerOpen,
      initialScorerTitle,
      weeklyPlanOpen,
    },
    actions: {
      setCoachOpen,
      setTitleScorerOpen,
      setWeeklyPlanOpen,
      openTitleScorerWith,
      addIdea,
      reload: loadAllData,
    },
  };
}
