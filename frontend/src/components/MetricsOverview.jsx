import React from 'react';
import { Users, Eye, Video, Award, TrendingUp, CheckCircle2 } from 'lucide-react';

export function MetricsOverview({ summary }) {
  if (!summary) return null;

  const watchTimePct = Math.min(100, Math.round((summary.watch_time_hours / summary.monetization_watch_target) * 100));
  const subPct = Math.min(100, Math.round((summary.subscriber_count / summary.monetization_sub_target) * 100));

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
      {/* 1. Channel Profile & Key Stats */}
      <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
        <div className="flex items-center gap-4">
          <img
            src={summary.avatar_url}
            alt={summary.channel_name}
            className="w-16 h-16 rounded-2xl border-2 border-indigo-500/40 object-cover shadow-lg shadow-indigo-500/20"
          />
          <div>
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              {summary.channel_name}
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            </h2>
            <p className="text-sm text-slate-400">{summary.handle}</p>
            <span className="inline-block mt-1 text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
              {summary.niche}
            </span>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-2 mt-6 pt-4 border-t border-slate-800/80">
          <div className="text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-xs">
              <Users className="w-3.5 h-3.5" />
              Subs
            </div>
            <div className="text-lg font-bold text-white mt-0.5">
              {summary.subscriber_count.toLocaleString()}
            </div>
          </div>
          <div className="text-center border-x border-slate-800">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-xs">
              <Eye className="w-3.5 h-3.5" />
              Views
            </div>
            <div className="text-lg font-bold text-white mt-0.5">
              {(summary.total_views / 1000000).toFixed(2)}M
            </div>
          </div>
          <div className="text-center">
            <div className="flex items-center justify-center gap-1 text-slate-400 text-xs">
              <Video className="w-3.5 h-3.5" />
              Videos
            </div>
            <div className="text-lg font-bold text-white mt-0.5">
              {summary.video_count}
            </div>
          </div>
        </div>
      </div>

      {/* 2. Growth Health Score (0-100) */}
      <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <Award className="w-5 h-5 text-indigo-400" />
              Growth Health Score
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">Weighted metric across 3 pillars</p>
          </div>
          <div className="text-right">
            <span className="text-3xl font-black bg-gradient-to-r from-emerald-400 to-indigo-400 bg-clip-text text-transparent">
              {summary.growth_health_score}
            </span>
            <span className="text-xs text-slate-400"> / 100</span>
          </div>
        </div>

        {/* Breakdown progress bars */}
        <div className="space-y-3 mt-4">
          <div>
            <div className="flex justify-between text-xs mb-1">
              <span className="text-slate-300">Upload Consistency (40%)</span>
              <span className="font-semibold text-emerald-400">{summary.health_breakdown?.consistency || 82}%</span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div
                className="h-full bg-emerald-500 rounded-full"
                style={{ width: `${summary.health_breakdown?.consistency || 82}%` }}
              />
            </div>
          </div>

          <div>
            <div className="flex justify-between text-xs mb-1">
              <span className="text-slate-300">Viewer Engagement (35%)</span>
              <span className="font-semibold text-indigo-400">{summary.health_breakdown?.engagement || 78}%</span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div
                className="h-full bg-indigo-500 rounded-full"
                style={{ width: `${summary.health_breakdown?.engagement || 78}%` }}
              />
            </div>
          </div>

          <div>
            <div className="flex justify-between text-xs mb-1">
              <span className="text-slate-300">Trend Alignment (25%)</span>
              <span className="font-semibold text-violet-400">{summary.health_breakdown?.trend_alignment || 88}%</span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div
                className="h-full bg-violet-500 rounded-full"
                style={{ width: `${summary.health_breakdown?.trend_alignment || 88}%` }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* 3. Monetization Readiness Tracker */}
      <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-emerald-400" />
              Monetization Readiness (YPP)
            </h3>
            <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              87% Ready
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">Tracking YouTube Partner Program targets</p>
        </div>

        <div className="space-y-4 my-3">
          {/* Subscribers target */}
          <div>
            <div className="flex justify-between text-xs mb-1">
              <span className="text-slate-300">Subscribers Goal</span>
              <span className="font-bold text-white">
                {summary.subscriber_count.toLocaleString()} / {summary.monetization_sub_target.toLocaleString()}
                <span className="ml-1 text-emerald-400">✓ Completed</span>
              </span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div className="h-full bg-emerald-400 rounded-full" style={{ width: '100%' }} />
            </div>
          </div>

          {/* Watch hours target */}
          <div>
            <div className="flex justify-between text-xs mb-1">
              <span className="text-slate-300">Watch Time Hours</span>
              <span className="font-bold text-indigo-300">
                {summary.watch_time_hours.toLocaleString()} / {summary.monetization_watch_target.toLocaleString()} hrs ({watchTimePct}%)
              </span>
            </div>
            <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden">
              <div className="h-full bg-gradient-to-r from-indigo-500 to-emerald-400 rounded-full" style={{ width: `${watchTimePct}%` }} />
            </div>
          </div>
        </div>

        <div className="bg-slate-800/50 rounded-xl p-2.5 text-[11px] text-slate-300 flex items-center justify-between">
          <span>🔥 Current Streak: <strong className="text-white">{summary.current_streak_weeks} weeks</strong></span>
          <span>Last Upload: <strong className="text-amber-400">{summary.last_upload_days_ago} days ago</strong></span>
        </div>
      </div>
    </div>
  );
}
