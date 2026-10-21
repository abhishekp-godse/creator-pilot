import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Navbar } from './components/Navbar';
import { NotificationBanner } from './components/NotificationBanner';
import { MetricsOverview } from './components/MetricsOverview';
import { GrowthForecastChart } from './components/GrowthForecastChart';
import { ContentGapFinder } from './components/ContentGapFinder';
import { TrendIntelligence } from './components/TrendIntelligence';
import { AICoachModal } from './components/AICoachModal';
import { TitleScorerModal } from './components/TitleScorerModal';
import { WeeklyPlanModal } from './components/WeeklyPlanModal';
import { RefreshCw, Sparkles, MessageCircle } from 'lucide-react';

export default function App() {
  const [summary, setSummary] = useState(null);
  const [notifications, setNotifications] = useState([]);
  const [forecast, setForecast] = useState(null);
  const [gaps, setGaps] = useState([]);
  const [videos, setVideos] = useState([]);
  const [trends, setTrends] = useState([]);
  const [loading, setLoading] = useState(true);

  // Modals state
  const [coachOpen, setCoachOpen] = useState(false);
  const [titleScorerOpen, setTitleScorerOpen] = useState(false);
  const [initialScorerTitle, setInitialScorerTitle] = useState('');
  const [weeklyPlanOpen, setWeeklyPlanOpen] = useState(false);

  const loadData = async () => {
    setLoading(true);
    try {
      const [sumRes, notifRes, foreRes, gapsRes, vidRes, trendsRes] = await Promise.all([
        axios.get('/api/channel/summary'),
        axios.get('/api/channel/notifications'),
        axios.get('/api/ml/growth-forecast'),
        axios.get('/api/gaps/content-gaps'),
        axios.get('/api/channel/videos'),
        axios.get('/api/trends/niche'),
      ]);

      setSummary(sumRes.data);
      setNotifications(notifRes.data);
      setForecast(foreRes.data);
      setGaps(gapsRes.data);
      setVideos(vidRes.data);
      setTrends(trendsRes.data);
    } catch (err) {
      console.error('Failed to load API data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const openTitleScorerWith = (title) => {
    setInitialScorerTitle(title);
    setTitleScorerOpen(true);
  };

  return (
    <div className="min-h-screen bg-[#0b0f19] text-slate-100 flex flex-col font-['Plus_Jakarta_Sans',sans-serif]">
      {/* Top Navbar */}
      <Navbar
        onOpenCoach={() => setCoachOpen(true)}
        onOpenTitleScorer={() => openTitleScorerWith('')}
        onOpenWeeklyPlan={() => setWeeklyPlanOpen(true)}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 py-6">
        {/* Proactive Alerts Bar */}
        <NotificationBanner notifications={notifications} />

        {loading ? (
          <div className="flex flex-col items-center justify-center py-24 text-slate-400 gap-3">
            <RefreshCw className="w-8 h-8 animate-spin text-indigo-500" />
            <p className="text-sm">Ingesting channel telemetry & syncing AI Coach...</p>
          </div>
        ) : (
          <>
            {/* 1. Channel Profile, Health Score, Monetization Readiness */}
            <MetricsOverview summary={summary} />

            {/* 2. 30-Day Predictive Growth Forecast (ML Prophet) */}
            <GrowthForecastChart forecast={forecast} />

            {/* 3. Trend Intelligence Engine */}
            <TrendIntelligence trends={trends} onSelectHook={openTitleScorerWith} />

            {/* 4. Content Gap Finder & Video Drop-off Hooks */}
            <ContentGapFinder
              gaps={gaps}
              videos={videos}
              onSelectTopic={openTitleScorerWith}
            />
          </>
        )}
      </main>

      {/* Floating Action Button for Voice Coach */}
      <button
        onClick={() => setCoachOpen(true)}
        className="fixed bottom-6 right-6 z-30 flex items-center gap-2 px-5 py-3.5 rounded-full bg-gradient-to-r from-indigo-600 via-indigo-500 to-violet-600 text-white font-bold shadow-xl shadow-indigo-600/40 hover:scale-105 active:scale-95 transition"
      >
        <Sparkles className="w-5 h-5 text-indigo-200 animate-spin" />
        <span>Ask AI Coach</span>
      </button>

      {/* Modals */}
      <AICoachModal isOpen={coachOpen} onClose={() => setCoachOpen(false)} />
      <TitleScorerModal
        isOpen={titleScorerOpen}
        onClose={() => setTitleScorerOpen(false)}
        initialTitle={initialScorerTitle}
      />
      <WeeklyPlanModal isOpen={weeklyPlanOpen} onClose={() => setWeeklyPlanOpen(false)} />

      {/* Footer */}
      <footer className="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500">
        CreatorPilot • AI Growth Coach & Decision Engine for Content Creators • Final Year Project
      </footer>
    </div>
  );
}
